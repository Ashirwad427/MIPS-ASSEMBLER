#run in linux terminal by java -jar Mars4_5.jar nc filename.asm(take inputs from console)

#system calls by MARS simulator:
#http://courses.missouristate.edu/kenvollmar/mars/help/syscallhelp.html
.data
	next_line: .asciiz "\n"
	inp_statement: .asciiz "Enter No. of integers to be taken as input: "
	inp_int_statement: .asciiz "Enter starting address of inputs(in decimal format): "
	out_int_statement: .asciiz "Enter starting address of outputs (in decimal format): "
	enter_int: .asciiz "Enter the integer: "	
.text
#input: N= how many numbers to sort should be entered from terminal. 
#It is stored in $t1
jal print_inp_statement	
jal input_int 
move $t1,$t4			

#input: X=The Starting address of input numbers (each 32bits) should be entered from
# terminal in decimal format. It is stored in $t2
jal print_inp_int_statement
jal input_int
move $t2,$t4

#input:Y= The Starting address of output numbers(each 32bits) should be entered
# from terminal in decimal. It is stored in $t3
jal print_out_int_statement
jal input_int
move $t3,$t4 

#input: The numbers to be sorted are now entered from terminal.
# They are stored in memory array whose starting address is given by $t2
move $t8,$t2
move $s7,$zero	#i = 0
loop1:  
	beq $s7,$t1,loop1end
	jal print_enter_int
	jal input_int
	sw $t4,0($t2)
	addi $t2,$t2,4
      	addi $s7,$s7,1
        j loop1      
loop1end: move $t2,$t8       
#############################################################
#Do not change any code above this line
#Occupied registers $t1,$t2,$t3. Don't use them in your sort function.
#############################################################
#function: should be written by students(sorting function)
#The below function adds 10 to the numbers. You have to replace this with
#your code

#Copying $t1, $t2 and $t3 to other locations
move $t6, $t1
move $s1, $t2
move $s2, $t3

#Copying the unsorted loop out output memory location
copy_loop:
	beq $s0, $t6, end_copy_loop
	lw $t4 0($s1)
	sw  $t4 ,0($s2)
	addi $s1,$s1,4
	addi $s2,$s2,4
    	addi $s0, $s0, 1
    	j copy_loop
end_copy_loop:
#Do nothing

#Sorting using bubble sort algorithm
bubble_sort:
    	addi $t6, $t6, -1		#to get 0 like indexing. i index starts from 0
    	move $s0, $zero
	addi $t7, $zero, 1		#making $t7 store a constant value 1 (to be used later)
	outer_loop:
    		beq $s0, $t6, end_outer_loop	#if outer_loop has run n times, end_outer_loop
    		move $s1, $zero
    		move $t5, $t3

	inner_loop:
		slt $t9, $s1, $t6	#if inner_loop has not run n times, set $t9 to 1
		beq $t9, $zero, end_inner_loop		#if $t9 is 0, then end loop as it has run n times
    		lw $s3, 0($t5)
    		lw $s4, 4($t5)
    		slt  $t8, $s3, $s4	#if element[i]<element[i+1], set $t8 to 1
    		beq $t8, $t7, no_swap		#if $t8 is 1, then dont swap
    		sw $s3, 4($t5)
    		sw $s4, 0($t5)

	no_swap:
    		addi $s1, $s1, 1
    		addi $t5, $t5, 4
    		
   		j inner_loop
    
	#Ending the inner_loop
	end_inner_loop:
    		addi $s0, $s0, 1
    		move $t5, $t3
    		
    		j outer_loop	#jumping back to outer_loop for next iteration

	#Ending the outer_loop
	end_outer_loop:
    		add $t6, $t6, 1
    		move $s0, $zero

#############################################################
#You need not change any code below this line

#print sorted numbers
move $s7,$zero	#i = 0
loop: beq $s7,$t1,end
      lw $t4,0($t3)
      jal print_int
      jal print_line
      addi $t3,$t3,4
      addi $s7,$s7,1
      j loop
#end
end:  li $v0,10
      syscall
#input from command line(takes input and stores it in $t6)
input_int: li $v0,5
	   syscall
	   move $t4,$v0
	   jr $ra
#print integer(prints the value of $t6 )
print_int: li $v0,1	
	   move $a0,$t4
	   syscall
	   jr $ra
#print nextline
print_line:li $v0,4
	   la $a0,next_line
	   syscall
	   jr $ra

#print number of inputs statement
print_inp_statement: li $v0,4
		la $a0,inp_statement
		syscall 
		jr $ra
#print input address statement
print_inp_int_statement: li $v0,4
		la $a0,inp_int_statement
		syscall 
		jr $ra
#print output address statement
print_out_int_statement: li $v0,4
		la $a0,out_int_statement
		syscall 
		jr $ra
#print enter integer statement
print_enter_int: li $v0,4
		la $a0,enter_int
		syscall 
		jr $ra
