# Slack IDLERPG bot

This charm deploys a Slack IDLERPG bot to run on your Slack Domain. It leverages
a docker container to ensure a consistent environment is used to run the script
in isolation.

## PreReq

Your Slack admin will need to
[enable the IRC Gateway, without SSL support](https://slack.zendesk.com/hc/en-us/articles/201727913-Connecting-to-Slack-over-IRC-and-XMPP).
This perl script connects to your slack domain through the IRC Gateway, and this
charm does not leverage the SSL support, as it requires stunnel. Contributions
welcome to enable this!

Your deployment environment will also need access to the docker public registry.

## Deployment

Deploying is as simple as:

    juju deploy cs:~lazypower/idlerpg


All config options are required to run the charm. `juju status-history` will
list any missing config options during deployment.

## Contact

 - Charm Author: [Charles Butler](mailto:charles.butler@ubuntu.com)


