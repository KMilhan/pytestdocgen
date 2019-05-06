###### Test Case: {{ name }}

* **Location**
    - `{{ file }}`@`{{ pos }}`

{% if summary %}
* **Summary**

{{ "" | indent(2, True, True) }}**{{ summary }}**

{% endif %}
{% if description %}
* **Description**

{{ description | indent(2, True, True) }}

{% endif %}
{% for section in sections %}
* {{ section }}

  {{  sections[section] | indent(2, True, True) }}

{% endfor %}
{% if  decorators %}
* **Decorated by**
{% for deco in decorators %}
    * `{{ deco }}`
{% endfor %}

{% endif %}
* **Signature and asserts**
  ```python
{{ snippet | indent(2, True, True)}}
  ```

