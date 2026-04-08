-- Auto Reset khi thấy [ERROR] You're already holding that egg
-- Dán vào Executor (Script Ware, Delta, Hydrogen, etc.)

local Players = game:GetService("Players")
local LocalPlayer = Players.LocalPlayer

local TARGET_TEXT = "already holding that egg"
local COOLDOWN = 5 -- giây chờ sau khi reset
local lastReset = 0
local resetCount = 0

-- Hàm reset nhân vật
local function resetCharacter()
    local now = tick()
    if now - lastReset < COOLDOWN then return end

    lastReset = now
    resetCount = resetCount + 1
    warn("[AutoReset] Phát hiện lỗi! Đang reset lần " .. resetCount .. "...")

    -- Cách 1: Dùng hàm có sẵn
    if LocalPlayer.Character then
        local humanoid = LocalPlayer.Character:FindFirstChildOfClass("Humanoid")
        if humanoid then
            humanoid.Health = 0
        end
    end

    -- Cách 2: Dùng Remote (backup nếu cách 1 bị chặn)
    -- game:GetService("Players").LocalPlayer:LoadCharacter()
end

-- Lắng nghe chat message (TextChatService)
local function hookTextChat()
    local ok, TextChatService = pcall(function()
        return game:GetService("TextChatService")
    end)
    if not ok then return end

    -- Roblox mới dùng TextChatService
    if TextChatService.MessageReceived then
        TextChatService.MessageReceived:Connect(function(msg)
            local text = msg.Text:lower()
            if text:find(TARGET_TEXT) then
                resetCharacter()
            end
        end)
        print("[AutoReset] Đã hook TextChatService ✓")
    end
end

-- Lắng nghe chat cũ (StarterGui Chat)
local function hookLegacyChat()
    local ok, StarterGui = pcall(function()
        return game:GetService("StarterGui")
    end)
    if not ok then return end

    -- Hook qua ChatGui nếu có
    local ChatGui = LocalPlayer.PlayerGui:WaitForChild("Chat", 5)
    if ChatGui then
        local Frame = ChatGui:FindFirstChild("Frame", true)
        if Frame then
            Frame.ChildAdded:Connect(function(child)
                task.wait(0.1)
                if child:IsA("TextLabel") or child:IsA("Frame") then
                    local label = child:FindFirstChildOfClass("TextLabel")
                    if label and label.Text:lower():find(TARGET_TEXT) then
                        resetCharacter()
                    end
                end
            end)
            print("[AutoReset] Đã hook Legacy Chat ✓")
        end
    end
end

-- Quét toàn bộ TextLabel trên màn hình (mạnh nhất)
local function scanScreenLabels()
    local PlayerGui = LocalPlayer:WaitForChild("PlayerGui")

    local function checkLabel(obj)
        if obj:IsA("TextLabel") or obj:IsA("TextButton") then
            if obj.Text:lower():find(TARGET_TEXT) then
                resetCharacter()
            end
        end
    end

    -- Theo dõi khi có UI mới xuất hiện
    local function watchDescendants(gui)
        gui.DescendantAdded:Connect(function(obj)
            task.wait(0.05)
            pcall(checkLabel, obj)
        end)
        -- Quét các label đang có sẵn
        for _, obj in ipairs(gui:GetDescendants()) do
            pcall(checkLabel, obj)
        end
    end

    watchDescendants(PlayerGui)

    -- Theo dõi GUI mới được thêm vào
    PlayerGui.ChildAdded:Connect(function(child)
        task.wait(0.1)
        watchDescendants(child)
    end)

    print("[AutoReset] Đã bật quét TextLabel màn hình ✓")
end

-- Quét định kỳ mỗi 1 giây (backup phòng miss)
local function periodicScan()
    local PlayerGui = LocalPlayer:WaitForChild("PlayerGui")
    task.spawn(function()
        while task.wait(1) do
            for _, obj in ipairs(PlayerGui:GetDescendants()) do
                if obj:IsA("TextLabel") or obj:IsA("TextButton") then
                    local ok, text = pcall(function() return obj.Text end)
                    if ok and text:lower():find(TARGET_TEXT) then
                        resetCharacter()
                        break
                    end
                end
            end
        end
    end)
    print("[AutoReset] Đã bật quét định kỳ 1s ✓")
end

-- ─── KHỞI ĐỘNG ───
print("=" .. string.rep("=", 40))
print("  Auto Reset - 'Already Holding That Egg'")
print("=" .. string.rep("=", 40))

pcall(hookTextChat)
pcall(hookLegacyChat)
pcall(scanScreenLabels)
pcall(periodicScan)

print("[AutoReset] Đang theo dõi... Nhân vật sẽ tự reset khi gặp lỗi!")
