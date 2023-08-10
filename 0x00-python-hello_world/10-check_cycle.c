#include "lists.h"

/**
 * check_cycle - check if there is a cycle in list
 * @list: pointer to list
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *h, *t;

	if (!list)
		return (0);

	h = list;
	t = list;
	while (h != NULL && h->next != NULL)
	{
		h = h->next->next;
		t = t->next;
		if (h == t)
			return (1);
	}
	return (0);
}
