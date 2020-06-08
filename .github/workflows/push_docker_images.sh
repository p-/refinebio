#!/bin/sh

REPO="docker.pkg.github.com/$GITHUB_REPOSITORY"
if [ -z "$IMAGES" ]; then
    echo "Error: must put images to pull in \$IMAGES" >&2
    exit 1
fi

for image in $IMAGES; do
    PACKAGE="$REPO/dr_$image"
    docker tag "ccdlstaging/dr_$image" "$PACKAGE"
    docker push "$PACKAGE"
done
