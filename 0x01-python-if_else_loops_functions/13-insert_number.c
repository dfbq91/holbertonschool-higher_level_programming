#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_number - insert a number into a sorted linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: number to insert in linked list
 * Return: adress of inserted number of NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;
	listint_t *after_current;

	current = *head;
	after_current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}

	after_current = after_current->next;

	while (after_current->next != NULL)
	{
		if (current->n > number)
		{
			new_node->next = current;
			*head = new_node;
			return (new_node);
		}
		if (after_current->n >= number)
		{
			new_node->next = after_current;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
		after_current = after_current->next;
	}
	new_node->next = NULL;
	after_current->next = new_node;

	return (new_node);
}
