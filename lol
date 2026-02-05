local Players = game:GetService("Players")

-- ===== DANH SÁCH TRẮNG (KHÔNG BỊ KICK) =====
local whitelist = {
	["bora21456"] = true,
	["bora145145"] = true,
	["boryluutru3"] = true,
	["vanhna4524"] = true,
	["btanloc13"] = true,
	["RoyalBra2008"] = true
}

local KICK_REASON = "Kiếm Script Khác Chơi Đi Con Mẹ Mày.!"

-- ===== HÀM KIỂM TRA & KICK =====
local function checkPlayer(player)
	if not whitelist[player.Name] then
		player:Kick(KICK_REASON)
	end
end

-- Kick toàn bộ người đang trong server (trừ whitelist)
for _, player in ipairs(Players:GetPlayers()) do
	checkPlayer(player)
end

-- Kick người vào sau
Players.PlayerAdded:Connect(function(player)
	checkPlayer(player)
end)


task.spawn(function()
    while task.wait(0.1) do
        local shared = workspace:FindFirstChild("DefaultMap_SharedInstances")
        if shared then
            local vip = shared:FindFirstChild("VIPWalls")
            if vip then
                vip:Destroy()
                warn("🔥 VIPWalls vừa spawn lại → xoá ngay")
            end
        end
    end
end)
