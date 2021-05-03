# Microsoft Azure CLI 'fzf' Extension

This package provides the fzf extension for Azure CLI, which allows use of the fzf interface to select defaults for certain items.

Currently supported:
- Subscription
- Resource group
- Location
- Customer name (via separate YAML file)

### Installation

```
python setup.py bdist_wheel
az extension add --yes  --source dist/fzf-1.0.3-py2.py3-none-any.whl
```

### Searching by customer name

YAML file to map customer names and subscription id should be a simple dictionary:
```
---
- customer: name1
  id: <subscription-id1>
  name: <subscription-name1>
- customer: name2
  id: <subscription-id2>
  name: <subscription-name2>
```

To generate the yaml from well-known public format for subscriptions use below one-liner:
```
cat subscriptions.md                 \
    | egrep '\w{8}-(\w{4}-){3}\w{12}'                                               \
    | perl -pe 's,\s*\|\s*,|,g;s,^\|\s+,,;s,\s*\|$,\n,;s,\t, ,g'                    \
    | awk -F\| '{ customer=$2; name=$3; if (length(customer) == 0) { customer="customer-"NR }; if (length(name) == 0) { name = customer } { print "- customer: "customer"\n  id: "$3"\n  name: "$4 } }'               \
    | yq e  > subscriptions.yml
```

and set `AZ_FZF_CUSTOMER_SUBSCRIPTIONS` environment variable to point to that file

```
export AZ_FZF_CUSTOMER_SUBSCRIPTIONS=/path/to/subscriptions.yml
```

### Support

Please note that this is a side project and is not officially supported by Microsoft. Please open any requests as issues on the project and do not call Microsoft support regarding this extension.
