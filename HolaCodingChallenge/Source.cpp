/* Copyright (C) Hola 2012, 2013
*
* Welcome to TheCodeIL.com Challenge!
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif


void str_cpy(char **s,const char* str)
{
	if (*s == NULL || strlen(*s)  != strlen(str))
	{
		*s = new char[strlen(str)];
		memset(*s, '\0', strlen(str) + 1);
	}
	memcpy(*s, str, strlen(str));
}
void str_cat(char** s, char* str)
{	
	if (*s == NULL)
	{
		*s = new char[strlen(str)];
		memset(*s, '\0', strlen(str) + 1);
	}
	strcat(*s, str);
 }


int main(int argc, char *argv[])
{
	char *s = new char[2];

	str_cpy(&s, "Hola Hola");
	
	str_cpy(&s, s + 5);
	str_cat(&s, " World");
	//str_printf(&s, "%s!", s);
	puts(s); /* result: "Hola World!" */
	//str_free(&s);
	return 0;
}
