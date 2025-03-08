
# Ansible Cheat Sheet

## 1. شروع با Ansible

### نصب Ansible
برای نصب Ansible بر روی اوبونتو:

```bash
sudo apt update
sudo apt install ansible
```

برای نصب در سایر سیستم‌ها، به [مستندات رسمی](https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html) مراجعه کنید.

### بررسی نسخه Ansible:
```bash
ansible --version
```

### پیکربندی Ansible:
فایل پیکربندی پیش‌فرض `ansible.cfg` است.

### فایل اینونتوری (Inventory)
یک فایل ساده به نام `inventory.ini` برای مشخص کردن میزبان‌ها ایجاد می‌شود.

```ini
[webservers]
web1 ansible_host=192.168.1.1
web2 ansible_host=192.168.1.2

[dbservers]
db1 ansible_host=192.168.1.3
```

### اجرای دستور بر روی همه میزبان‌ها
```bash
ansible all -m ping -i inventory.ini
```

## 2. دستورات Ansible

### اجرای Playbook
```bash
ansible-playbook playbook.yml
```

### اجرای دستور ساده با `ansible`
```bash
ansible all -m command -a "uptime" -i inventory.ini
```

### اجرای دستور از طریق `ansible ad-hoc`
```bash
ansible all -m shell -a 'df -h' -i inventory.ini
```

## 3. Playbook

### ساختار یک Playbook
```yaml
- name: Install Nginx
  hosts: webservers
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### اجرای Playbook:
```bash
ansible-playbook -i inventory.ini playbook.yml
```

## 4. مدیریت بسته‌ها

### نصب بسته:
```yaml
- name: Install a package
  apt:
    name: nginx
    state: present
```

### حذف بسته:
```yaml
- name: Remove a package
  apt:
    name: nginx
    state: absent
```

## 5. مدیریت کاربران و گروه‌ها

### ایجاد کاربر:
```yaml
- name: Create a user
  user:
    name: testuser
    state: present
    groups: sudo
```

### حذف کاربر:
```yaml
- name: Remove a user
  user:
    name: testuser
    state: absent
```

### اضافه کردن کاربر به گروه:
```yaml
- name: Add user to a group
  user:
    name: testuser
    group: sudo
```

## 6. مدیریت سرویس‌ها

### شروع یک سرویس:
```yaml
- name: Start nginx service
  service:
    name: nginx
    state: started
```

### توقف یک سرویس:
```yaml
- name: Stop nginx service
  service:
    name: nginx
    state: stopped
```

### فعال کردن سرویس در بوت:
```yaml
- name: Enable nginx service to start on boot
  service:
    name: nginx
    enabled: yes
```

## 7. متغیرها

### تعریف متغیرها:
```yaml
- name: Example playbook
  hosts: webservers
  vars:
    my_variable: "value"
  tasks:
    - name: Print a variable
      debug:
        msg: "The value is {{ my_variable }}"
```

### استفاده از متغیرها از فایل‌ها:
```yaml
- name: Example playbook
  hosts: webservers
  vars_files:
    - vars.yml
  tasks:
    - name: Print a variable
      debug:
        msg: "The value is {{ my_variable }}"
```

## 8. شرایط و حلقه‌ها

### استفاده از شرط‌ها:
```yaml
- name: Install nginx if not present
  apt:
    name: nginx
    state: present
  when: ansible_facts['os_family'] == 'Debian'
```

### استفاده از حلقه:
```yaml
- name: Install multiple packages
  apt:
    name: "{{ item }}"
    state: present
  loop:
    - nginx
    - git
    - curl
```

## 9. Handlers

### تعریف Handler:
```yaml
- name: Restart nginx if configuration changes
  service:
    name: nginx
    state: restarted
  notify:
    - Restart nginx
```

### تعریف و اجرای Handlers:
```yaml
handlers:
  - name: Restart nginx
    service:
      name: nginx
      state: restarted
```

## 10. برچسب‌ها (Tags)

### استفاده از Tags:
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx package
      apt:
        name: nginx
        state: present
      tags:
        - install
    - name: Start nginx service
      service:
        name: nginx
        state: started
      tags:
        - start
```

### اجرای Playbook با Tags:
```bash
ansible-playbook -i inventory.ini playbook.yml --tags "install"
```

## 11. رول‌ها (Roles)

### ساختار رول‌ها:
```bash
ansible-galaxy init myrole
```

این دستور یک ساختار پایه برای رول ایجاد می‌کند.

## 12. Template‌ها

### استفاده از Template:
```yaml
- name: Deploy configuration file
  template:
    src: /templates/nginx.conf.j2
    dest: /etc/nginx/nginx.conf
```

### قالب Jinja2 در Template:
```jinja
server {
    listen 80;
    server_name {{ server_name }};
    root {{ root_dir }};
}
```

## 13. فایل‌های شامل (Includes)

### استفاده از Include:
```yaml
- name: Include another playbook
  include: other_playbook.yml
```

## 14. اعتبارسنجی و لاگ‌ها

### استفاده از `debug` برای چاپ اطلاعات:
```yaml
- name: Debugging a variable
  debug:
    msg: "The variable value is {{ my_variable }}"
```

### ثبت لاگ‌ها:
```yaml
- name: Log message to file
  lineinfile:
    path: /var/log/ansible.log
    line: "Task completed successfully"
```

## 15. متغیرهای داخلی Ansible

- `ansible_facts`: اطلاعات مربوط به سیستم هدف.
- `inventory_hostname`: نام میزبان در فهرست موجودیت.
- `ansible_user`: نام کاربری که به سیستم هدف وارد شده است.

## 16. گروه‌ها

### تعریف گروه‌ها در Inventory:
```ini
[webservers]
web1
web2

[dbservers]
db1
db2
```

### استفاده از گروه‌ها در Playbook:
```yaml
- name: Playbook for web servers
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

---

این چیت شیت شامل دستورات، نکات و روش‌های معمول استفاده از Ansible است. امیدوارم برای شما مفید باشد.
