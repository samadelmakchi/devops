# Bash

```bash
#!/usr/bin/env bash

name="John"
echo "Hello $name!"
```

### متغیرها

```bash
name="John"
echo $name       # مشاهده پایین
echo "$name"
echo "${name}!"
```

به طور کلی متغیرهای خود را محصور کنید مگر اینکه شامل wildcardها برای گسترش یا بخش‌های دستوری باشند.

```bash
wildcard="*.txt"
options="iv"
cp -$options $wildcard /tmp
```

### نقل قول‌های رشته‌ای

```bash
name="John"
echo "Hi $name"  #=> Hi John
echo 'Hi $name'  #=> Hi $name
```

### اجرای شل

```bash
echo "I'm in $(pwd)"
echo "I'm in `pwd`"  # obsolescent
# Same
```

### اجرای مشروط

```bash
git commit && git push
git commit || echo "Commit failed"
```

### توابع

```bash
get_name() {
  echo "John"
}

echo "You are $(get_name)"
```

### شرط ها

```bash
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
fi
```

### حالت سختگیرانه

```bash
set -euo pipefail
IFS=$'\n\t'
```

### انبساط بریس

```bash
echo {A,B}.js
```

| Expression             | Description           |
| ---------------------- | --------------------- |
| `{A,B}`                | Same as `A B`         |
| `{A,B}.js`             | Same as `A.js B.js`   |
| `{1..5}`               | Same as `1 2 3 4 5`   |
| <code>&lcub;{1..3},{7..9}}</code> | Same as `1 2 3 7 8 9` |

## پارامترها

### مبانی

```bash
name="John"
echo "${name}"
echo "${name/J/j}"    #=> "john" (substitution)
echo "${name:0:2}"    #=> "Jo" (slicing)
echo "${name::2}"     #=> "Jo" (slicing)
echo "${name::-1}"    #=> "Joh" (slicing)
echo "${name:(-1)}"   #=> "n" (slicing from right)
echo "${name:(-2):1}" #=> "h" (slicing from right)
echo "${food:-Cake}"  #=> $food or "Cake"
```

```bash
length=2
echo "${name:0:length}"  #=> "Jo"
```

```bash
str="/path/to/foo.cpp"
echo "${str%.cpp}"    # /path/to/foo
echo "${str%.cpp}.o"  # /path/to/foo.o
echo "${str%/*}"      # /path/to

echo "${str##*.}"     # cpp (پسوند)
echo "${str##*/}"     # foo.cpp (مسیر پایه)

echo "${str#*/}"      # path/to/foo.cpp
echo "${str##*/}"     # foo.cpp

echo "${str/foo/bar}" # /path/to/bar.cpp
```

```bash
str="Hello world"
echo "${str:6:5}"    # "world"
echo "${str: -5:5}"  # "world"
```

```bash
src="/path/to/foo.cpp"
base=${src##*/}   #=> "foo.cpp" (مسیر پایه)
dir=${src%$base}  #=> "/path/to/" (مسیر مستقیم)
```

### گسترش نام پیشوند

```bash
prefix_a=one
prefix_b=two
echo ${!prefix_*}  # نام همه متغیرها که با "پیشوند_" شروع می شود
prefix_a prefix_b
```

### غیر جهت

```bash
name=joe
pointer=name
echo ${!pointer}
joe
```

### تعویض

| Code              | Description         |
| ----------------- | ------------------- |
| `${foo%suffix}`   | Remove suffix       |
| `${foo#prefix}`   | Remove prefix       |
| ---               | ---                 |
| `${foo%%suffix}`  | Remove long suffix  |
| `${foo/%suffix}`  | Remove long suffix  |
| `${foo##prefix}`  | Remove long prefix  |
| `${foo/#prefix}`  | Remove long prefix  |
| ---               | ---                 |
| `${foo/from/to}`  | Replace first match |
| `${foo//from/to}` | Replace all         |
| ---               | ---                 |
| `${foo/%from/to}` | Replace suffix      |
| `${foo/#from/to}` | Replace prefix      |

### کامنت ها

```bash
# Single line comment
```

```bash
: '
This is a
multi line
comment
'
```

### رشته های فرعی

| Expression      | Description                    |
| --------------- | ------------------------------ |
| `${foo:0:3}`    | Substring _(position, length)_ |
| `${foo:(-3):3}` | Substring from the right       |

### طول

| Expression | Description      |
| ---------- | ---------------- |
| `${#foo}`  | Length of `$foo` |

### دستکاری

```bash
str="HELLO WORLD!"
echo "${str,}"   #=> "hELLO WORLD!" (lowercase 1st letter)
echo "${str,,}"  #=> "hello world!" (all lowercase)

str="hello world!"
echo "${str^}"   #=> "Hello world!" (uppercase 1st letter)
echo "${str^^}"  #=> "HELLO WORLD!" (all uppercase)
```

### مقادیر پیش فرض

| Expression        | Description                                              |
| ----------------- | -------------------------------------------------------- |
| `${foo:-val}`     | `$foo`, or `val` if unset (or null)                      |
| `${foo:=val}`     | Set `$foo` to `val` if unset (or null)                   |
| `${foo:+val}`     | `val` if `$foo` is set (and not null)                    |
| `${foo:?message}` | Show error message and exit if `$foo` is unset (or null) |

حذف `:`، بررسی های (غیر) بی اعتباری را حذف می کند، به عنوان مثال. `${foo-val}` اگر تنظیم نشود در غیر این صورت `$foo` به `val` گسترش می‌یابد.

## حلقه ها

### پایه برای حلقه

```bash
for i in /etc/rc.*; do
  echo "$i"
done
```

### حلقه هایشبیه زبان C

```bash
for ((i = 0 ; i < 100 ; i++)); do
  echo "$i"
done
```

### محدوده ها

```bash
for i in {1..5}; do
    echo "Welcome $i"
done
```

#### با اندازه پله

```bash
for i in {5..50..5}; do
    echo "Welcome $i"
done
```

### خواندن خطوط

```bash
while read -r line; do
  echo "$line"
done <file.txt
```

### برای همیشه

```bash
while true; do
  ···
done
```

## توابع

### تعریف توابع

```bash
myfunc() {
    echo "hello $1"
}
```

```bash
function myfunc {
    echo "hello $1"
}
```

```bash
myfunc "John"
```

### برگرداندن مقادیر

```bash
myfunc() {
    local myresult='some value'
    echo "$myresult"
}
```

```bash
result=$(myfunc)
```

### بالا بردن خطاها

```bash
myfunc() {
  return 1
}
```

```bash
if myfunc; then
  echo "success"
else
  echo "failure"
fi
```

### آرگومان ها

| بیان       | توضیحات                                             |
| ---------- | --------------------------------------------------- |
| `$#`       | تعداد آرگومان ها                                    |
| `$*`       | همه آرگومان های موضعی (به عنوان یک کلمه)            |
| `$@`       | همه آرگومان های موقعیتی (به عنوان رشته های جداگانه) |
| `$1`       | آرگومان اول                                         |
| `$_`       | آخرین آرگومان دستور قبلی                            |

**توجه**: `$@` و `$*` باید نقل قول شوند تا مطابق شرح داده شوند.
در غیر این صورت، آنها دقیقاً همان کار را انجام می دهند (استدلال ها به عنوان رشته های جداگانه).

## شرط ها

### شرط ها

Note that `[[` is actually a command/program that returns either `0` (true) or `1` (false). Any program that obeys the same logic (like all base utils, such as `grep(1)` or `ping(1)`) can be used as condition, see examples.

| Condition                | Description           |
| ------------------------ | --------------------- |
| `[[ -z STRING ]]`        | رشته خالی            |
| `[[ -n STRING ]]`        | رشته خالی نیست       |
| `[[ STRING == STRING ]]` | برابر                |
| `[[ STRING != STRING ]]` | برابر نیست           |
| ---                      | ---                   |
| `[[ NUM -eq NUM ]]`      | برابر                 |
| `[[ NUM -ne NUM ]]`      | برابر نیست           |
| `[[ NUM -lt NUM ]]`      | کمتر از              |
| `[[ NUM -le NUM ]]`      | کمتر یا مساوی        |
| `[[ NUM -gt NUM ]]`      | بزرگتر از            |
| `[[ NUM -ge NUM ]]`      | بزرگتر یا مساوی      |
| ---                      | ---                   |
| `[[ STRING =~ STRING ]]` | عبارت منظم           |
| ---                      | ---                   |
| `(( NUM < NUM ))`        | شرط های عددی         |

#### شرط های بیشتر

| Condition            | Description              |
| -------------------- | ------------------------ |
| `[[ -o noclobber ]]` | If OPTIONNAME is enabled |
| ---                  | ---                      |
| `[[ ! EXPR ]]`       | Not                      |
| `[[ X && Y ]]`       | And                      |
| `[[ X || Y ]]`       | Or                       |

### File conditions

| Condition               | Description             |
| ----------------------- | ----------------------- |
| `[[ -e FILE ]]`         | Exists                  |
| `[[ -r FILE ]]`         | Readable                |
| `[[ -h FILE ]]`         | Symlink                 |
| `[[ -d FILE ]]`         | Directory               |
| `[[ -w FILE ]]`         | Writable                |
| `[[ -s FILE ]]`         | Size is > 0 bytes       |
| `[[ -f FILE ]]`         | File                    |
| `[[ -x FILE ]]`         | Executable              |
| ---                     | ---                     |
| `[[ FILE1 -nt FILE2 ]]` | 1 is more recent than 2 |
| `[[ FILE1 -ot FILE2 ]]` | 2 is more recent than 1 |
| `[[ FILE1 -ef FILE2 ]]` | Same files              |

### مثال

```bash
# String
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
else
  echo "This never happens"
fi
```

```bash
# Combinations
if [[ X && Y ]]; then
  ...
fi
```

```bash
# Equal
if [[ "$A" == "$B" ]]
```

```bash
# Regex
if [[ "A" =~ . ]]
```

```bash
if (( $a < $b )); then
   echo "$a is smaller than $b"
fi
```

```bash
if [[ -e "file.txt" ]]; then
  echo "file exists"
fi
```

---

## آرایه

### تعریف آرایه ها

```bash
Fruits=('Apple' 'Banana' 'Orange')
```

```bash
Fruits[0]="Apple"
Fruits[1]="Banana"
Fruits[2]="Orange"
```

### کار با آرایه ها

```bash
echo "${Fruits[0]}"           # Element #0
echo "${Fruits[-1]}"          # Last element
echo "${Fruits[@]}"           # All elements, space-separated
echo "${#Fruits[@]}"          # Number of elements
echo "${#Fruits}"             # String length of the 1st element
echo "${#Fruits[3]}"          # String length of the Nth element
echo "${Fruits[@]:3:2}"       # Range (from position 3, length 2)
echo "${!Fruits[@]}"          # Keys of all elements, space-separated
```

### عملیات

```bash
Fruits=("${Fruits[@]}" "Watermelon")    # Push
Fruits+=('Watermelon')                  # Also Push
Fruits=( "${Fruits[@]/Ap*/}" )          # Remove by regex match
unset Fruits[2]                         # Remove one item
Fruits=("${Fruits[@]}")                 # Duplicate
Fruits=("${Fruits[@]}" "${Veggies[@]}") # Concatenate
lines=(`cat "logfile"`)                 # Read from file
```

### تکرار

```bash
for i in "${arrayName[@]}"; do
  echo "$i"
done
```

## دیکشنری ها

### تعریف کردن

```bash
declare -A sounds
```

```bash
sounds[dog]="bark"
sounds[cow]="moo"
sounds[bird]="tweet"
sounds[wolf]="howl"
```

`sound` را به عنوان یک شی دیکشنری (معروف به آرایه انجمنی) اعلام می کند.

### کار با دیکشنری ها

```bash
echo "${sounds[dog]}" # Dog's sound
echo "${sounds[@]}"   # All values
echo "${!sounds[@]}"  # All keys
echo "${#sounds[@]}"  # Number of elements
unset sounds[dog]     # Delete dog
```

### تکرار

#### Iterate over values

```bash
for val in "${sounds[@]}"; do
  echo "$val"
done
```

#### تکرار روی کلیدها

```bash
for key in "${!sounds[@]}"; do
  echo "$key"
done
```

## آپشن ها

### آپشن ها

```bash
set -o noclobber  # Avoid overlay files (echo "hi" > foo)
set -o errexit    # Used to exit upon error, avoiding cascading errors
set -o pipefail   # Unveils hidden failures
set -o nounset    # Exposes unset variables
```

### آپشن های عمومی

```bash
shopt -s nullglob    # Non-matching globs are removed  ('*.foo' => '')
shopt -s failglob    # Non-matching globs throw errors
shopt -s nocaseglob  # Case insensitive globs
shopt -s dotglob     # Wildcards match dotfiles ("*.sh" => ".foo.sh")
shopt -s globstar    # Allow ** for recursive matches ('lib/**/*.rb' => 'lib/a/b/c.rb')
```

`GLOBIGNORE` را به‌عنوان فهرستی از الگوهای جدا شده با دو نقطه تنظیم کنید تا از موارد مشابه حذف شوند.

## تاریخچه

### دستورات

| Command               | Description                               |
| --------------------- | ----------------------------------------- |
| `history`             | Show history                              |
| `shopt -s histverify` | Don't execute expanded result immediately |

### بسط ها

| Expression   | Description                                          |
| ------------ | ---------------------------------------------------- |
| `!$`         | Expand last parameter of most recent command         |
| `!*`         | Expand all parameters of most recent command         |
| `!-n`        | Expand `n`th most recent command                     |
| `!n`         | Expand `n`th command in history                      |
| `!<command>` | Expand most recent invocation of command `<command>` |

### عملیات

| Code                 | Description                                                           |
| -------------------- | --------------------------------------------------------------------- |
| `!!`                 | Execute last command again                                            |
| `!!:s/<FROM>/<TO>/`  | Replace first occurrence of `<FROM>` to `<TO>` in most recent command |
| `!!:gs/<FROM>/<TO>/` | Replace all occurrences of `<FROM>` to `<TO>` in most recent command  |
| `!$:t`               | Expand only basename from last parameter of most recent command       |
| `!$:h`               | Expand only directory from last parameter of most recent command      |

`!!` and `!$` can be replaced with any valid expansion.

### برش ها

| Code     | Description                                                                              |
| -------- | ---------------------------------------------------------------------------------------- |
| `!!:n`   | Expand only `n`th token from most recent command (command is `0`; first argument is `1`) |
| `!^`     | Expand first argument from most recent command                                           |
| `!$`     | Expand last token from most recent command                                               |
| `!!:n-m` | Expand range of tokens from most recent command                                          |
| `!!:n-$` | Expand `n`th token to last from most recent command                                      |

`!!` can be replaced with any valid expansion i.e. `!cat`, `!-2`, `!42`, etc.

## متفرقه

### محاسبات عددی

```bash
$((a + 200))      # Add 200 to $a
```

```bash
$(($RANDOM%200))  # Random number 0..199
```

```bash
declare -i count  # Declare as type integer
count+=1          # Increment
```

### زیر پوسته ها

```bash
(cd somedir; echo "I'm now in $PWD")
pwd # still in first directory
```

### تغییر مسیر

```bash
python hello.py > output.txt            # stdout to (file)
python hello.py >> output.txt           # stdout to (file), append
python hello.py 2> error.log            # stderr to (file)
python hello.py 2>&1                    # stderr to stdout
python hello.py 2>/dev/null             # stderr to (null)
python hello.py >output.txt 2>&1        # stdout and stderr to (file), equivalent to &>
python hello.py &>/dev/null             # stdout and stderr to (null)
echo "$0: warning: too many users" >&2  # print diagnostic message to stderr
```

```bash
python hello.py < foo.txt      # feed foo.txt to stdin for python
diff <(ls -r) <(ls)            # Compare two stdout without files
```

### بازرسی دستورات

```bash
command -V cd
#=> "cd is a function/alias/whatever"
```

### خطاها را تله کنید

```bash
trap 'echo Error at about $LINENO' ERR
```

or

```bash
traperr() {
  echo "ERROR: ${BASH_SOURCE[1]} at about ${BASH_LINENO[0]}"
}

set -o errtrace
trap traperr ERR
```

### Case/switch

```bash
case "$1" in
  start | up)
    vagrant up
    ;;

  *)
    echo "Usage: $0 {start|stop|ssh}"
    ;;
esac
```

### Source relative

```bash
source "${0%/*}/../share/foo.sh"
```

### printf

```bash
printf "Hello %s, I'm %s" Sven Olga
#=> "Hello Sven, I'm Olga

printf "1 + 1 = %d" 2
#=> "1 + 1 = 2"

printf "This is how you print a float: %f" 2
#=> "This is how you print a float: 2.000000"

printf '%s\n' '#!/bin/bash' 'echo hello' >file
# format string is applied to each group of arguments
printf '%i+%i=%i\n' 1 2 3  4 5 9
```

### تبدیل رشته ها

| Command option | Description                                         |
| -------------- | --------------------------------------------------- |
| `-c`           | Operations apply to characters not in the given set |
| `-d`           | Delete characters                                   |
| `-s`           | Replaces repeated characters with single occurrence |
| `-t`           | Truncates                                           |
| `[:upper:]`    | All upper case letters                              |
| `[:lower:]`    | All lower case letters                              |
| `[:digit:]`    | All digits                                          |
| `[:space:]`    | All whitespace                                      |
| `[:alpha:]`    | All letters                                         |
| `[:alnum:]`    | All letters and digits                              |

#### مثال

```bash
echo "Welcome To Devhints" | tr '[:lower:]' '[:upper:]'
WELCOME TO DEVHINTS
```

### دایرکتوری اسکریپت

```bash
dir=${0%/*}
```

### دریافت آپشن ها

```bash
while [[ "$1" =~ ^- && ! "$1" == "--" ]]; do case $1 in
  -V | --version )
    echo "$version"
    exit
    ;;
  -s | --string )
    shift; string=$1
    ;;
  -f | --flag )
    flag=1
    ;;
esac; shift; done
if [[ "$1" == '--' ]]; then shift; fi
```

### هردوک

```sh
cat <<END
hello world
END
```

### خواندن ورودی

```bash
echo -n "Proceed? [y/n]: "
read -r ans
echo "$ans"
```

The `-r` option disables a peculiar legacy behavior with backslashes.

```bash
read -n 1 ans    # Just one character
```

### متغیرهای خاص

| Expression         | Description                            |
| ------------------ | -------------------------------------- |
| `$?`               | Exit status of last task               |
| `$!`               | PID of last background task            |
| `$$`               | PID of shell                           |
| `$0`               | Filename of the shell script           |
| `$_`               | Last argument of the previous command  |
| `${PIPESTATUS[n]}` | return value of piped commands (array) |

### به دایرکتوری قبلی بروید

```bash
pwd # /home/user/foo
cd bar/
pwd # /home/user/foo/bar
cd -
pwd # /home/user/foo
```

### نتیجه فرمان را بررسی کنید

```bash
if ping -c 1 google.com; then
  echo "It appears you have a working internet connection"
fi
```

### گرپ چک

```bash
if grep -q 'foo' ~/.bash_history; then
  echo "You appear to have typed 'foo' in the past"
fi
```
