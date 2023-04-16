.PHONY = run
up :
	docker compose up -d 

# Restarts JUST the Python Container hosting Flask 
.PHONY = apprestart
apprestart :
	docker compose restart web


