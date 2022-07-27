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

### Install the feedbackapi Python library

Then, within a docker container or a virtualenv , do
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

### Run the tests
Having completed the steps above, it should now be possible to run the tests, with:
```bash
aws-vault exec moj-lpa-dev -- pytest
```
Again it is necessary to use aws-vault so that the test can get the secret from Secrets Manager to use against the test api
