unit qsort; 
	interface
	
	implementation
		const max = 100;{ const max = 50;
		type list = array[1..max] of integer; 
		var data: list; 
		i: integer; 
	
	procedure quicksort(var a: list; Lo,Hi: integer); 
				
		procedure sort(l,r: integer);
			 
			var 
				i,j,x,y: integer; 
				 
			begin
			
				i:=l; 
				j:=r; 
				x:=a[(l+r) DIV 2]; 
				repeat 
					while a[i]<x do 
						i:=i+1;
					
					while x<a[j] do 
						j:=j-1;
					
					if i<=j then
					begin
						y:=a[i]; a[i]:=a[j]; a[j]:=y;
						i:=i+1; j:=j-1;
						end;
					until i>j;
				
				if l<j 
				then
					sort(l,j); 
					 
				if i<r 
				then
					sort(i,r); 
					 
				end;
		begin {quicksort};
			sort(Lo,Hi);
			end;
			
			
	
	begin {qsort}
		writeln;
		writeln;
		Write('Now generating some random numbers...');{Write('Now generating 1000 random numbers...');
		writeln;
		Randomize;
		for i:=1 to max do begin
			data[i]:=Random(30000);
			Write(data[i]:8);{Randomize;
			end;
		
		writeln;
		writeln;
		Write('Now sorting random numbers...');
		writeln;
		quicksort(data,1,max);
		for i:=1 to max do
			Write(data[i]:8);{Randomize;
					
		end.
		
		
{  Export  Date: 11:18:11 PM - 16:Jul:2025}

