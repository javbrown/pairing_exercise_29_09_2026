## 1 problem - user story
```
As a member of a group chat,
I want the chat's participants shown as a single readable line,
so that I can see at a glance who's in the conversation.

Acceptance criteria:

No participants: the line is empty.
[] => ""

One participant: just their name.
["Bart"] => "Bart"

Two participants: joined with an ampersand.
["Bart", "Lisa"] => "Bart & Lisa"

Three or more participants: commas between names, with an ampersand before the last one.
["Bart", "Lisa", "Maggie"] => "Bart, Lisa & Maggie"

Order is kept: names appear in the same order they were given.
```
## 2 function signature
```python
# Parameters:
# - list of names
# Return type:
# - string of names 
# Side Effects:
# - 
def single_readable_line():
    pass
```

## 3 exampples
```python
# scenario 1
single_readable_line() => an empty string ""
# scenario 2
single_readable_line(['bob']) => "bob"
# scenario 3
single_readable_line(['Bob', 'bart']) => "bob & bart"
4
single_readable_line(more that three names) => " name with commas, and & before last name"