##
## EPITECH PROJECT, 2022
## Makefile
## File description:
## Groundhog
##

D_SRC	=	./src/

NAME	=	autoCompletion

$(NAME)	:
		cp ./src/main.py ./
		mv main.py autoCompletion
		chmod +x autoCompletion

all	:	$(NAME)


clean:
		rm -rf autoCompletion

fclean:	clean

re	:	fclean all

.PHONY: all clean fclean re
