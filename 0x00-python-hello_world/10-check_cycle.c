#include "lists.h"

/**
 * check_cycle - check if a linked list is a cycle.
 * @head: head of linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *head)
{
	listint_t *tortoise = head;
	listint_t *hare = head;

	while (tortoise && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}
