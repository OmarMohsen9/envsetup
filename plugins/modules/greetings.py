
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    result = {
        'changed': False,
        'msg': "Hello"
    }

    module.exit_json(**result)

if __name__ == '__main__':
    main()
