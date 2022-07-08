# opg-feedback
Development repository: Managed by opg-org-infra &amp; Terraform

opg-feedback-apps provides a resuable component collect feedback information for the performance platform.  There is currently just an api. A front-end form using Jinja templates, is to follow shortly. The api library includes database connections (postgres supported so far), basic healthcheck, AWS xray, and will soon include authentication. The intended use is to have endpoints plugged in. (See [opg feedback repo](https://github.com/ministryofjustice/opg-feedback) for an example).

## Installation

### Clone repo

Download this repo via:

```bash
git clone https://github.com/ministryofjustice/opg-feedback.git
cd opg-feedback
```

### Install the Python library

Then, within a docker container or a virtualenv , do
```bash
cd feedbackapi
pip install -e .
```
