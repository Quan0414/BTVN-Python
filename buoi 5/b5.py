docker_compose = {
    "version": "3.8",
    "services": {
        "app": {
            "image": "python:3.10-slim",
            "command": "python app.py",
            "volumes": "./app:/app",
            "restart": "always",
            "ports": "5000:5000",
            "depends_on": "db"
        }
    }
}

print(docker_compose)

docker_compose["version"] = "3.10"
print(docker_compose)

print(f"image_value: {docker_compose['services']['app']['image']}")

docker_compose["services"]["app"]["environment"] = ["PYTHONUNBUFFERED=1"]
print(docker_compose)

has_volumes = "volumes" in docker_compose["services"]["app"]
print(has_volumes)

del docker_compose["services"]["app"]["depends_on"]
print(docker_compose)

key_count = len(docker_compose)
print(key_count)

all_values = list(docker_compose.values())
print(all_values)

contains_always = "always" in str(docker_compose.values())
print(contains_always)

new_key = input()
new_value = input()
docker_compose[new_key] = new_value
print(docker_compose)