#! /usr/local/bin/bash
# > ./packages.sh
# list all installed packages that contain substrings "apps", "cs" or "ba" separated with "->"

packages=""

# traverse through all packages [macos command]
for pkg in $(pkgutil --pkgs)
do
    # put package name in lowercase
    lowercase_pkg="${pkg,,}"

    # check if package name contains substrings "apps", "cs" or "ba"
    if [[ $lowercase_pkg =~ "apps" || $lowercase_pkg =~ "cs" || $lowercase_pkg =~ "ba" ]]
    then
        # append package name to the output string
        packages+=$pkg"->"
    fi
done

# check if there is at least one package
if [ -n "$packages" ]
then
    # display packages without the last 2-character-long separator
    echo ${packages::-2}
else 
    # display empty string as there are no packages
    echo ""
fi
