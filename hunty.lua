-- HACKBORY - Hunty Zombies Script
-- Auto Spam JoinSession + Zombie Hitbox Extender + Auto Press Z/G

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

-- ⚡ Hitbox Extender cho Zombie NPC
task.spawn(function()
    while task.wait(0.1) do
        for _, mob in pairs(workspace:GetDescendants()) do
            if mob:IsA("Model") and mob:FindFirstChild("Humanoid") and mob:FindFirstChild("HumanoidRootPart") then
                if mob.Name:lower():find("zombie") then
                    local hrp = mob.HumanoidRootPart
                    hrp.Size = Vector3.new(500, 500, 500) -- tăng hitbox
                    hrp.Transparency = 1 -- ẩn đi
                    hrp.CanCollide = false
                    hrp.Massless = true
                end
            end
        end
    end
end)

-- ⚡ Auto bấm phím Z mỗi 10 giây
local VirtualInputManager = game:GetService("VirtualInputManager")
task.spawn(function()
    while task.wait(10) do
        pcall(function()
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.Z, false, game)
            task.wait(0.1)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.Z, false, game)
        end)
    end
end)

-- ⚡ Auto bấm phím G mỗi 2 phút (120 giây)
task.spawn(function()
    while task.wait(100) do
        pcall(function()
            VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.G, false, game)
            task.wait(0.1)
            VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.G, false, game)
        end)
    end
end)

-- ♾️ Dòng lặp bật script vô hạn (tự khởi động lại)
while true do
    pcall(function()
        loadstring(game:HttpGet("https://raw.githubusercontent.com/BRYSHADOW/BRY/refs/heads/main/hunty.lua"))()
    end)
    task.wait(1) -- chờ 5s rồi chạy lại, tránh spam quá nhanh
end
