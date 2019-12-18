#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *currentA;
	listint_t *currentB;
	listint_t *temp;
	int nnodes = 1;
	int i = 0;

	if (*head == NULL)
		return (1);

	currentA = *head;
	currentB = *head;
	temp = *head;

	currentB = currentB->next;

	while (currentB->next != NULL)
	{
		currentB = currentB->next;
		temp = temp->next;
		nnodes++;
	}

	for (i = 0; i < nnodes / 2; i++)
	{
		if (currentA->n != currentB->n)
			return (0);
		if (currentA->n == currentB->n)
		{
			currentA = currentA->next;
			currentB = temp;
			temp = currentA;

			while (temp->next != currentB)
				temp = temp->next;
		}
		if (currentB->n == temp->n)
			return (1);
	}

	return (1);

}
