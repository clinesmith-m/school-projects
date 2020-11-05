fun printIntList(lst) =
    print(ListFormat.listToString (fn i => Int.toString(i)) lst ^ "\n")

fun head([]) = 0
|   head(h::t) = h

fun tail([]) = []
|   tail(h::t) = t

fun diags_safe(x, check_val, []) = true
|   diags_safe(x, check_val, h::t) =
    if (x + check_val) = h then
        false
    else
        if (x - check_val) = h then
            false
        else
            diags_safe(x, (check_val+1), t)

fun val_safe(x, []) = true
|   val_safe(x, h::t) =
    if x = h then
        false
    else
        val_safe(x, t)

fun rows_safe([]) = true
|   rows_safe(h::t) = 
    if val_safe(h, t) then
        rows_safe(t)
    else
        false

fun safe(n, []) = true
|   safe(n, h::t) =
    if h <= n then
        if rows_safe((h::t)) then
            if diags_safe(h, 1, t) then
                true
            else
                false
        else
            false
    else
        false

fun nqueenslist(n, lst) = 
    if safe(n, lst) then
        if length(lst) = n then
            lst
        else
            nqueenslist(n, 1::lst)
    else
        if safe(n, (1+head(lst))::tail(lst)) then
            nqueenslist(n, (1+head(lst))::tail(lst))
        else
            if head(lst) < n then
                nqueenslist(n, (2+head(lst))::tail(lst))
            else
                nqueenslist(n, (1+head(tail(lst)))::tail(tail(lst)))

fun nqueens n = nqueenslist(n, [])
