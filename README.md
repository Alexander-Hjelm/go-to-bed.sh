# go-to-bed.sh
Still up at 2 AM? Time for some good ol' spartan discipline! >:)

# How to
Assuming go-to-bed.sh is placed at the top of your user's ~-directory, Add the following sudo cronjob:

@reboot sh \~/go-to-bed.sh/go-to-bed.sh >\~/go-to-bed.sh/logs/cronlog 2>&1

Now reboot and enjoy
