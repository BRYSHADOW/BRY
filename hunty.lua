local VirtualInputManager = game:GetService("VirtualInputManager")

-- ⚡ Auto ấn Z + load script GitHub
task.spawn(function()
    while true do
        pcall(function()
            -- Ấn Z
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.Z, false, game)
            task.wait(0.1)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.Z, false, game)

            -- Đợi 10s
            task.wait(10)

            -- Chạy script GitHub
            loadstring(game:HttpGet("https://raw.githubusercontent.com/BRYSHADOW/BRY/refs/heads/main/hunty.lua"))()
        end)

        -- Đợi thêm 10s nữa trước khi lặp lại (tổng = 20s 1 vòng)
        task.wait(10)
    end
end)

-- ⚡ Auto spam JoinSession
local args = { true } -- true = CÓ, false = KHÔNG
task.spawn(function()
    while task.wait(1) do
        pcall(function()
            game:GetService("ReplicatedStorage")
                :WaitForChild("Packets")
                :WaitForChild("JoinSession")
                :InvokeServer(unpack(args))
        end)
    end
end)
