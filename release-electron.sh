#!/bin/bash -e

cd agent-app

update_version() {
  echo "$(node -p "p=require('./${1}');p.version='${2}';JSON.stringify(p,null,2)")" > $1
  echo "Updated ${1} version to ${2}"
}

current_version=$(node -p "require('./package').version")

printf "Next version (current is $current_version)? "
read next_version

next_ref="v$next_version"

update_version 'package.json' $next_version

git commit --allow-empty -am "Version $next_version"

git tag $next_ref

git push origin master
git push --tags
