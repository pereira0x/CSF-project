import subprocess
import urllib.parse
import datetime

IPs = {
        "194.210.61.135": "Rafael Calhau",
        "194.210.61.134": "Virgolino Gonçalves",
        "94.210.61.136": "Miguel Estrela",
        "194.210.63.254": "Router",
        "10.0.2.15": "Router (Public IP)",
}

def resolve_ip(ip):
    return IPs.get(ip, ip)

def resolve_host(host):
    for ip, name in IPs.items():
        if host == name:
            return ip

def run_tshark(filters, fields, extra_flags = "", filename = "trace.pcapng"):
    def escape_filter(f):
        return f
    cmd = ["tshark", "-r", filename, "-T", "fields", "-Y '", escape_filter(filters), "'"]
    for field in fields:
        cmd.extend(["-e", field])
    cmd = ' '.join(cmd)
    cmd += " " + extra_flags
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = p.communicate()
    return output[0].decode('utf-8').split('\n')[:-1]

def urldecode(url):
    return urllib.parse.unquote_plus(url)

def extract_urlencoded_parameter(url, parameter):
    return urldecode(url.split(parameter + '=')[1].split('&')[0])

def convert_time(time):
    # convert epoch time
    date = datetime.datetime.fromtimestamp(float(time))
    date = date - datetime.timedelta(weeks=2)
    date = date.strftime("%Y-%m-%d %H:%M:%S")
    return date
