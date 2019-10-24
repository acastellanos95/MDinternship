module io
    implicit none
    integer(8)::N, i, j, l, AllocateStatus
    real(4)::Lx, Ly, Lz
    ! posicion y velocidad en 3D
    real(4), dimension(:), allocatable :: Rx, Ry, Rz
    real(4), dimension(:), allocatable :: Vx, Vy, Vz

    contains
        subroutine input(filein)
            implicit none
            character(15)::filein
            open(10, file = filein)
            ! Leer N
            read(10,*) N
            allocate ( Rx(N), Ry(N), Rz(N), Vx(N), Vy(N), Vz(N), STAT = AllocateStatus)
            if (AllocateStatus /= 0) STOP "*** Not enough memory ***"
            ! imprimir N
            print *, 'N', N
            ! Leer  dimension de la caja de simulacion
            read(10,*) Lx, Ly, Lz
            ! imprimir la dimension
            print *, 'X Y Z', Lx, Ly, Lz
            ! Iterar en posiciones y velocidades para asignaciones
            do 1 i=1,N
                read(10,*) j, Rx(i), Ry(i), Rz(i), Vx(i), Vy(i), Vz(i)
                print *, j, 'pos', Rx(i), Ry(i), Rz(i), 'vel', Vx(i), Vy(i), Vz(i)
            1 end do
            close(10)
        end subroutine input
        subroutine output(fileout)
            character(15)::fileout
            open(11, file = fileout)
            write(11,*) N
            write(11,*) Lx, Ly, Lz
            do 2 l=1,N
                write(11,*) l, Rx(l), Ry(l), Rz(l), Vx(l), Vy(l), Vz(l)
                print *, l, 'pos', Rx(l), Ry(l), Rz(l), 'vel', Vx(l), Vy(l), Vz(l)
            2 end do
            close(11)
        end subroutine output
end module io