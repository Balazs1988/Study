# Authentication by using SSH keys

In the followings, we can show how can we create SSH key pair for GitLab authentication, and how to use them.

## Generate new key pair

```commandline
$ ssh-keygen -t ed25519 -a 100 -f ~/.ssh/gitlab_key
```

* On Windows system the path can be different.
* It is advised to use a passphrase.
* For checking the keys, see the ``~/.ssh`` directory!

## Using the SSH agent

Start the SSH agent:
```commandline
$ eval $(ssh-agent)
```

Add private key to the agent:
```commandline
$ ssh-add ~/.ssh/gitlab_key
```

List the added identities:
```commandline
$ ssh-add -L
```

## Adding public key to GitLab

You have to add your public key to GitLab for successful authentication.
* Navigate to (personal) Preferences.
* Select ``SSH Keys`` on the left side.
* Add the content of the ``~/.ssh/gitlab_key.pub`` to the text field.

## Cloning the repository

When you clone the repository, you should choose the URL which started with ``git@gitlab``.
