# OPTED Tutorial Website

*Built with [Quarto](https://quarto.org/)*

This repository contains the raw build files for the OPTED Tutorial website ([tutorials.opted.eu](https://tutorials.opted.eu/)) 

# Build

Run

```
quarto render tutorial_website
```

# Deploy

```
rsync -r --info=progress2 tutorial_website/_site/ user@server:/path/to/www/
```

# nginx config


```
server {
	listen 80;
	server_name tutorials.opted.eu;
	return 301 https://tutorials.opted.eu$request_uri;
}


server {
	server_name tutorials.opted.eu;

	listen 443 ssl;
	ssl_certificate /path/to/cert.pem;
	ssl_certificate_key /path/to/key.key;

	root /path/to/html;


	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}

}

```