from shlex import split
from subprocess import check_call
from subprocess import check_output

from charms.reactive import set_state
from charms.reactive import when
from charms.reactive import when_not

from charmhelpers.core.hookenv import config
from charmhelpers.core.hookenv import status_set
from charmhelpers.core.templating import render
from os import getcwd


@when('docker.available')
@when_not('idlerpg.available')
def config_changed():
    status_set("maintenance", "Pulling IdleRPG Container")
    cmd = "docker pull lazypower/idlerpg"
    check_call(split(cmd))
    set_state('idlerpg.available')
    setup_persistent_data()
    status_set("maintenance", "")


@when('idlerpg.available')
def run_container():
    # Abort if no configuration
    if not check_config():
        return

    render_config()

    # Check for container existence
    cmd = "docker inspect idlerpg"
    try:
        run(cmd)
        running = True
    except:
        # The service is not running
        running = False

    if running:
        run("docker kill idlerpg")
        run("docker rm idlerpg")

    cwd = getcwd()
    cmd = "docker run --restart=always --name idlerpg -d -v {}/data:/idlerpg/data lazypower/idlerpg".format(cwd)  # noqa
    docker_id = check_output(split(cmd))
    run("payload-register docker slackbot {}".format(docker_id))
    status_set("active", "IdleRPG Bot running")


def render_config():
    cfg = config()
    render('irpg.conf', 'data/.irpg.conf', cfg)


def check_config():
    cfg = config()
    keys = ['slackserver',
            'slackpassword',
            'botnick',
            'botname',
            'botrealname',
            'botchan',
            'botowner']
    for k in keys:
        if not cfg.get(k):
            status_set("blocked", "Missing Configuration for: {}".format(k))
            return False
    return True


def setup_persistent_data():
    cmd = "scripts/setup_idlerpg.sh"
    run(cmd)


def run(cmd):
    check_call(split(cmd))
