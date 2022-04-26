# Check the repository size via bash cmd and github API

echo "torvards linux"
curl -s https://api.github.com/repos/torvalds/linux | jq '.size' | numfmt --to=iec --from-unit=1024

echo "Awesome Java"
curl -s https://github.com/akullpp/awesome-java | jq '.size' | numfmt --to=iec --from-unit=1024

# For the private repos uncomment below
# curl -s -H "Authorization: token GITHUB_TOKEN" https://api.github.com/repos/torvalds/linux | jq '.size' | numfmt --to=iec --from-unit=1024
