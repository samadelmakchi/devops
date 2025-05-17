
# Terraform 

### 🛠 مقدمه

Terraform ابزار Infrastructure as Code (IaC) از شرکت HashiCorp است که اجازه می‌دهد زیرساخت‌های ابری را به صورت دکلراسیو تعریف و مدیریت کنید.

---

### 📦 نصب Terraform

#### روی Linux:
```bash
wget https://releases.hashicorp.com/terraform/1.7.5/terraform_1.7.5_linux_amd64.zip
unzip terraform_1.7.5_linux_amd64.zip
sudo mv terraform /usr/local/bin/
terraform -v
```

#### روی macOS:
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

---

### 🗂 ساختار پروژه

```bash
project/
├── main.tf              # منابع اصلی
├── variables.tf         # تعریف متغیرها
├── outputs.tf           # خروجی‌ها
├── terraform.tfvars     # مقادیر متغیرها
├── provider.tf          # تعریف providerها
└── modules/             # ماژول‌های خارجی یا داخلی
```

---

### 🔧 دستورات اصلی Terraform

| دستور | توضیح |
|-------|-------|
| `terraform init` | مقداردهی اولیه پروژه و نصب provider ها |
| `terraform validate` | بررسی اعتبار فایل‌های HCL |
| `terraform plan` | نمایش تغییراتی که قرار است اعمال شود |
| `terraform apply` | اعمال تغییرات در زیرساخت |
| `terraform destroy` | حذف تمام منابع تعریف‌شده |
| `terraform fmt` | فرمت‌ کردن فایل‌های `.tf` |
| `terraform show` | نمایش وضعیت منابع جاری |
| `terraform output` | نمایش خروجی‌های تعریف‌شده |
| `terraform state` | مدیریت فایل state |
| `terraform taint` | علامت‌گذاری یک resource برای بازسازی |
| `terraform import` | وارد کردن منابع موجود به Terraform |

---

### ☁ تعریف Provider (مثال AWS)

```hcl
provider "aws" {
  region  = "us-east-1"
  profile = "default"
}
```

---

### 🌳 تعریف Resource

```hcl
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type

  tags = {
    Name = "MyEC2Instance"
  }
}
```

---

### 📥 تعریف Variable

```hcl
variable "instance_type" {
  description = "Type of EC2 instance"
  type        = string
  default     = "t2.micro"
}
```

در `terraform.tfvars` مقداردهی:

```hcl
instance_type = "t3.small"
```

---

### 📤 تعریف Output

```hcl
output "instance_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.example.public_ip
}
```

---

### 🔐 مدیریت State

#### فایل `terraform.tfstate`:
- شامل وضعیت فعلی زیرساخت
- نباید به صورت دستی ویرایش شود

#### Remote State (S3 + DynamoDB):
```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "global/dev/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

---

### 📦 استفاده از ماژول‌ها

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "4.0.2"

  name = "main-vpc"
  cidr = "10.0.0.0/16"
}
```

---

### 🧪 شرایط (Conditionals)

```hcl
instance_type = var.is_production ? "t3.large" : "t2.micro"
```

---

### 🔁 حلقه‌ها

```hcl
resource "aws_security_group_rule" "allow_ports" {
  count = length(var.ports)
  from_port   = var.ports[count.index]
  to_port     = var.ports[count.index]
  protocol    = "tcp"
  ...
}
```

---

### 📄 فایل `.terraform.lock.hcl`

- قفل کردن نسخه provider برای تکرارپذیری (reproducibility)

---

### 🛠 ابزارهای مفید

- `tflint`: بررسی lint و قوانین کدنویسی
- `checkov`: آنالیز امنیتی
- `tfsec`: بررسی آسیب‌پذیری منابع
- `pre-commit hooks`: اجرای خودکار فرمت و تست‌ها قبل از commit

---

### 🧠 نکات حرفه‌ای

- همیشه از `terraform plan` قبل از `apply` استفاده کن
- از Remote backend برای همکاری تیمی استفاده کن
- منابع حساس مثل secret ها را در `tfvars` قرار نده
- از ماژول‌ها برای کد قابل استفاده مجدد استفاده کن
