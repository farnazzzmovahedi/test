1. Basic Info
name → Name of the app shown in the UI, e.g., "WordPress", "Nextcloud".
slug → A URL-friendly version of the name, e.g., "wordpress", "nextcloud".
description → Short description of the app.
icon → Image URL or upload path for the app icon.
type → ForeignKey to ApplicationType → defines template defaults, build options, envs, etc.
2. Image & Registry
application → Reference to Application model → defines the image, ports, mounts, and envs.
builder → Reference to Builder → which builds the image if not already built.
registery → Container registry where the image is stored (Registery table).
harbor_user → Credentials for private registry (HarborRegistryUser).
image_tag → Optional pre-defined tag if you want to deploy a specific version.
3. Project / Deployment Info
project_item → ProjectItem to which this one-click app will belong.
volume / volume_bind → If the app needs storage, point to a preconfigured Volume.
service / service_port → If the app exposes ports, reference Service and port configuration.
namespace → Usually inherited from Project or ProjectItem.
4. Config / Secrets
configmaps → Optional ConfigMap objects prefilled for the app.
secrets → Optional Secret objects (DB passwords, API keys).

envs → Optional env variables specific to the app.
Example:

{"DB_HOST": "localhost", "DB_USER": "root"}
5. Domains / Ingress
project_domain → Reference to ProjectDomains if the app needs a domain.
non_www → Boolean for www redirect handling.
ssl → Enum, e.g., "Http", "Free", "Custom".
6. Optional Features
database_management → Preconfigured DB if needed (reference DatabaseManagment).
file_manager → Preconfigured file storage if needed (reference FileManager).
enable_socket → Boolean if this app uses WebSocket (used in some apps like chat apps).
preinstalled_files → List of files or volumes that should be mounted automatically.
default_envs → Defaults for one-click deployment, can come from ApplicationType.
7. Example Record for WordPress
OneClickApp.objects.create(
    name="WordPress",
    slug="wordpress",
    description="One-click WordPress app",
    icon="icons/wordpress.png",
    type=ApplicationType.objects.get(slug="php-wordpress"),
    application=Application.objects.get(name="wordpress-app"),
    builder=Builder.objects.get(location="us-east"),
    registery=Registery.objects.get(url="registry.example.com"),
    harbor_user=HarborRegistryUser.objects.get(username="user1"),
    project_item=ProjectItem.objects.get(name="my-project-wordpress"),
    volume=Volume.objects.get(name="wordpress-data"),
    service=Service.objects.get(name="wordpress-service"),
    service_port=ServicePort.objects.get(port=80),
    project_domain=ProjectDomains.objects.get(domain__name="wordpress.example.com"),
    ssl="Free",
    enable_socket_for_domain=False,
    database_management=DatabaseManagment.objects.get(deployment_name="wp-db"),
    file_manager=FileManager.objects.get(deployment_name="wp-files"),
    default_envs={"WP_DB_HOST": "wp-db", "WP_DB_USER": "root", "WP_DB_PASSWORD": "pass"},
)