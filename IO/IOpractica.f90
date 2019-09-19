program main
    use IO
    implicit none

    !File names
    character(len=15)::filein, fileout

    !request for input file name and perform input operations
    write(*,*) "Enter file input: "
    read(*,*) filein
    call Input(filein)

    !request for output file name and perform output operations
    write(*,*) "Enter output file name: "
    read(*,*) fileout
    call Output(fileout)


end program main