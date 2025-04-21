# Markdown <a name="TOP"></a>

# سرفصل 1 #

    Markup :  # Heading 1 #

    -OR-

    Markup :  ============= (below H1 text)

## سرفصل 2 ##

    Markup :  ## Heading 2 ##

    -OR-

    Markup: --------------- (below H2 text)

### سرفصل 3 ###

    Markup :  ### Heading 3 ###

#### سرفصل 4 ####

    Markup :  #### Heading 4 ####


متن مشترک

    Markup :  Common text

_متن تاکید شده_

    Markup :  _Emphasized text_ or *Emphasized text*

~~متن خط خورده~~

    Markup :  ~~Strikethrough text~~

__متن قوی__

    Markup :  __Strong text__ or **Strong text**

___متن تاکیدی قوی___

    Markup :  ___Strong emphasized text___ or ***Strong emphasized text***

[نام لینک](https://www.google.com/ "عنوان لینک نامگذاری شده") and https://www.google.com/ or <https://elmakchi.ir/>

    Markup :  [Named Link](http://www.google.fr/ "Named link title") and http://www.google.fr/ or <http://example.com/>

[عنوان-1](#heading-1 "رفتن به عنوان-1")
    
    Markup: [heading-1](#heading-1 "Goto heading-1")

جدول, شبیه این یکی :

سربرگ اول  |     سربرگ دوم
------------- | -------------
محتوای سلول  |   محتوای سلول
محتوای سلول  |   محتوای سلول

```
سربرگ اول  |     سربرگ دوم
------------- | -------------
محتوای سلول  |   محتوای سلول
محتوای سلول  |   محتوای سلول
```

افزودن یک لوله `|` در یک سلول:

سربرگ اول  |     سربرگ دوم
------------- | -------------
محتوای سلول  |   محتوای سلول
محتوای سلول   | \|

```
سربرگ اول  |     سربرگ دوم
------------- | -------------
محتوای سلول  |   محتوای سلول
محتوای سلول   |  \| 
```

جدول تراز چپ، راست و وسط

سربرگ تراز چپ | سربرگ تراز راست | سربرگ تراز شده در مرکز
| :--- | ---: | :---:
محتوای سلول  | محتوای سلول | محتوای سلول
محتوای سلول  | محتوای سلول | محتوای سلول

```
سربرگ تراز چپ | سربرگ تراز راست| سربرگ تراز شده در مرکز
| :--- | ---: | :---:
محتوای سلول  | محتوای سلول | محتوای سلول
محتوای سلول  | محتوای سلول | محتوای سلول
```

`code()`

    Markup :  `code()`

```javascript
    var specificLanguage_code = 
    {
        "data": {
            "lookedUpPlatform": 1,
            "query": "Kasabian+Test+Transmission",
            "lookedUpItem": {
                "name": "Test Transmission",
                "artist": "Kasabian",
                "album": "Kasabian",
                "picture": null,
                "link": "http://open.spotify.com/track/5jhJur5n4fasblLSCOcrTp"
            }
        }
    }
```

    Markup : ```javascript
             ```

* Bullet list
    * Nested bullet
        * Sub-nested bullet etc
* Bullet list item 2

~~~
 Markup : * Bullet list
              * Nested bullet
                  * Sub-nested bullet etc
          * Bullet list item 2

-OR-

 Markup : - Bullet list
              - Nested bullet
                  - Sub-nested bullet etc
          - Bullet list item 2 
~~~

1. A numbered list
    1. A nested numbered list
    2. Which is numbered
2. Which is numbered

~~~
 Markup : 1. A numbered list
              1. A nested numbered list
              2. Which is numbered
          2. Which is numbered
~~~

- [ ] An uncompleted task
- [x] A completed task

~~~
 Markup : - [ ] An uncompleted task
          - [x] A completed task
~~~

- [ ] An uncompleted task
    - [ ] A subtask

~~~
 Markup : - [ ] An uncompleted task
              - [ ] A subtask
~~~

> بلوک نقل قول
>> بلوک نقل قول تو در تو

    Markup :  > Blockquote
              >> Nested Blockquote

_خط افقی :_
- - - -

    Markup :  - - - -

_تصویر با متن جایگزین :_

![متن جایگزین تصویر](https://avatars.githubusercontent.com/u/6169366?v=4 "عنوان اختیاری است")

    Markup : ![picture alt](https://avatars.githubusercontent.com/u/6169366?v=4 "Title is optional")

متن تاشو:

<details>
  <summary>عنوان 1</summary>
  <p>محتوا 1 محتوا 1 محتوا 1 محتوا 1 محتوا 1</p>
</details>
<details>
  <summary>عنوان 2</summary>
  <p>محتوا 2 محتوا 2 محتوا 2 محتوا 2 محتوا 2</p>
</details>

    Markup : <details>
               <summary>Title 1</summary>
               <p>Content 1 Content 1 Content 1 Content 1 Content 1</p>
             </details>

```html
<h3>HTML</h3>
<p> Some HTML code here </p>
```

پیوند به بخش خاصی از صفحه:

[Go To TOP](#TOP)
   
    Markup : [text goes here](#section_name)
              section_title<a name="section_name"></a>    

کلید فوری:

<kbd>⌘F</kbd>

<kbd>⇧⌘F</kbd>

    Markup : <kbd>⌘F</kbd>

لیست کلیدهای فوری:

| Key | Symbol |
| --- | --- |
| Option | ⌥ |
| Control | ⌃ |
| Command | ⌘ |
| Shift | ⇧ |
| Caps Lock | ⇪ |
| Tab | ⇥ |
| Esc | ⎋ |
| Power | ⌽ |
| Return | ↩ |
| Delete | ⌫ |
| Up | ↑ |
| Down | ↓ |
| Left | ← |
| Right | → |


