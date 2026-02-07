local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local LocalPlayer = Players.LocalPlayer

-- ===== DANH SÁCH TRẮNG (KHÔNG BỊ KICK) =====
local whitelist = {
	["bora21456"] = true,
	["bora145145"] = true,
	["alexrykhuvuon"] = true,
	["vanhna4524"] = true,
	["btanloc13"] = true,
	["RoyalBra2008"] = true
}

local KICK_REASON = "Vui Lòng Liên Hệ Admin AlexRyVipPro để Mở khoá (yk:10base và 10 voi dâu)"

-- ===== AUTO CHAT NẾU LÀ btanloc13 =====
if LocalPlayer and LocalPlayer.Name == "btanloc13" then
	task.spawn(function()
		for i = 1, 5 do
			ReplicatedStorage.DefaultChatSystemChatEvents.SayMessageRequest:FireServer(
				"Anh AlexRyVipPro ĐZVL",
				"All"
			)
			task.wait(0.8) -- delay nhẹ tránh spam quá nhanh
		end
	end)
end

-- ===== HÀM KIỂM TRA & KICK =====
local function checkPlayer(player)
	local nameLower = string.lower(player.Name)

	-- Nếu tên có chữ "alexry" thì bỏ qua (không kick)
	if string.find(nameLower, "alexy") then
		return
	end

	-- Nếu không có trong whitelist thì kick
	if not whitelist[player.Name] then
		player:Kick(KICK_REASON)
	end
end

-- Kick toàn bộ người đang trong server
for _, player in ipairs(Players:GetPlayers()) do
	checkPlayer(player)
end

-- Kick người vào sau
Players.PlayerAdded:Connect(function(player)
	checkPlayer(player)
end)
