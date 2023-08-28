# Easy_Git

## About Project-
Easy_Git provide users an Interface that helps then use git more easily.
Input is taken as an English statement and the selection of commands is done with keywords.

Example Inputs-> "Initialize repo", "push my changes", "commit".

It is to be noted that commands are matched in the same order they are given below.

# Keyword mapping-

## Change working directory->
'change' in query and ('folder' in query or 'directory' in query)

## Show current directory->
"current" in query or 'working' in query or "directory" in query

## Change operation mode( speech\text)->
 ("change" in query or "switch" in query )and "mode" in query

## Initialize repository
'init' in query or 'initialize' in query

##  Push changes->
'push' in query

## Pull command->
"pull" in query

## Add remote repository->
'remote' in query

## Create new branch->
('new' in query or 'create' in query) and 'branch' in query

## Change branch->
('change' in query  and 'branch' in query) or 'checkout' in query

## Add or stage changes->
"add" in query or "stage" in query) and 'remote' not in query

##  Status command->
"status" in query

## Check logs->
"log" in query or "logs" in query

## Commit changes->
"commit" in query

## Reset changes->
"reset" in query



