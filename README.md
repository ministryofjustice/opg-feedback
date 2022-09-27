# opg-feedback
Development repository: Managed by opg-org-infra &amp; Terraform

opg-feedback-apps provides a re-usable component which will collect feedback from users, for the performance platform.  There is currently just an api. A front-end form using Jinja templates, is to follow shortly. The api library includes database connections (postgres supported so far), basic healthcheck, AWS xray, and will soon include authentication. The intended use is to have endpoints plugged in. (See [opg feedback repo](https://github.com/ministryofjustice/opg-feedback) for an example).

## Installation

### Clone repo

Download this repo via:

```bash
git clone https://github.com/ministryofjustice/opg-feedback.git
cd opg-feedback
```

### Make a virtualenv if needed
If you are working in a docker container you can skip the virtualenv step, but if running locally, a virtualenv is helpful:
```bash
virtualenv ~/feedbackapienv
source ~/feedbackapienv/bin/activate
```

### Install the feedbackapi Python library

Then, within a docker container or the virtualenv created above, do
```bash
cd feedbackapi
pip install -e .
```


### Spin up the stack

The stack, of 3 containers - postgres, feedbackdb which populates postgres, and feedbackapi,  can be started with:
```bash
aws-vault exec moj-lpa-dev -- docker-compose up
```
The requirement for aws-vault is because the Bearer Token for the api is stored in AWS Secrets Manager
Note that the postgres container will be exposed on the standard 5432 port, so appear like a locally running postgres on the host. Before starting up, please ensure you do not already have a locally running postgres on standard 5432 port, otherwise tests will fail,

### Run the tests
To run the tests it is necessary to install requests and pytest in the virtual env:
```bash
pip install pytest requests
```

If you fail to do that step it may try to use an existing pytest from the system python and cause import failures

Having completed the steps above, it should now be possible to run the tests, with:
```bash
export POSTGRES_NAME=lpadb POSTGRES_PASSWORD=lpapass POSTGRES_USERNAME=lpauser POSTGRES_HOSTNAME=postgres
aws-vault exec moj-lpa-dev -- pytest
```
Again it is necessary to use aws-vault so that the test can get the secret from Secrets Manager to use against the test api
