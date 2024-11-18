hook.Add("KeyPress", "HandleKeyPress", function(ply, key)
    if key  ==  then
        ply:ChatPrint("Вы прыгнули!")
    end
end)