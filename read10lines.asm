extern printf
extern fopen
extern freadline
extern fclose
extern fgets

section .rodata ; initialized data
mode : db "r",0
output : db "%c",0
new : db "",10,0

section .bss ; uninitialized data
fp : resd 1; 4bytes
buffer : resb 1;1 byte
fn : resd 1 ;4bytes
n : resb 1

section .data
i : db 0
j : db 0

section .text

global main

main:
	
	push ebp
	mov ebp,esp

	mov esi,DWORD[ebp+8];argc
	mov edi,DWORD[ebp+12];argv
	cmp esi,1
	je .exit

	mov edx,[edi+4];second argument ie file name
	mov [fn],edx
	push mode
	push DWORD[fn]
	call fopen
	add esp,8
	mov DWORD[fp],eax;file pointer
	test eax,eax
	jz .exit ; file cannot be opened

.oloop:	
	
	xor eax,eax
	push DWORD[fp] ; file pointer
	push 100 ;size
	push buffer ; string pointed to buffer
	call fgets
	xor ebx,ebx
	mov ebx,eax ; if fgets is success, it returns buffer in eax.
	add esp,12
	
	
.iloop:	
	
	push DWORD[ebx]
	push output
	call printf
	add esp,8
	inc ebx
	cmp BYTE[ebx],0xa
	jne .iloop
	push new ; print newline
	call printf
	add esp,4
	inc DWORD[i]
	xor ecx,ecx
	mov ecx,DWORD[i] ; counter
	cmp ecx ,10 ; 10 lines of file
	jl .oloop
	push DWORD[fp]
    	call fclose
    	    
.exit:

	
	xor eax,eax
	leave
	ret	
