def validate_ip(ip_address):
    import re
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    return re.match(ip_pattern, ip_address) is not None
