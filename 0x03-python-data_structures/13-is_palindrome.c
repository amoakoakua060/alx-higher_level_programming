#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - is a linked list a palindrome or not
 * @head: head of linked list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int *stack = NULL;
	int size = 0, mid = 0, i = 0;
	listint_t *node = NULL;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	node = *head;
	while (node != NULL)
	{
		size++;
		node = node->next;
	}

	stack = malloc(sizeof(int) * size);
	node = *head;
	while (node != NULL)
	{
		stack[i] = node->n;
		i++;
		node = node->next;
	}

	if (size % 2 != 0)
		mid = (size + 1) / 2;
	else
		mid = size / 2;

	for (i = 0; i != mid; i++)
		if (stack[i] != stack[size - 1 - i])
		{
			free(stack);
			return (0);
		}

	free(stack);
	return (1);
}
