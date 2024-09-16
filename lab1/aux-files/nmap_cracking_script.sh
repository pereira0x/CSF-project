dd if=../csf-lab1-artifacts/nmap of=nmap_cracked bs=1 skip=64
base64 -d nmap_cracked | xxd -r -p > ../secrets/ist_ids_dump
rm nmap_cracked
cat ../secrets/ist_ids_dump
