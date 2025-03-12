# YAML

### لغت نامه ها و فهرست ها

```yaml
# کامنت با "#" شروع می شود
# فرهنگ لغت مانند "key: value" نوشته می شود
name: Martin D'vloper
languages:
  perl: Elite
  python: Elite
  pascal: Lame

# لیست موارد که با "-" شروع می شود
foods:
  - Apple
  - Orange
  - Strawberry
  - Mango

# بولی ها با حروف کوچک هستند
employed: true
```

### رشته های چند خطی

```yaml
# اسکالر بلاک تحت اللفظی
Multiline: |
  exactly as you see
  will appear these three
  lines of poetry
```

```yaml
# بلوک اسکالر تا شده
Multiline: <
  this is really a
  single line of text
  despite appearances
```

### ارث بری

```yaml
parent: &defaults
  a: 2
  b: 3

child:
  <<: *defaults
  b: 4
```

### محتوای مرجع

```yaml
values: &ref
  - These values
  - will be reused below
  
other_values:
  <<: *ref
```
