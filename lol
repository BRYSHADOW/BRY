local Players = game:GetService("Players")

-- ===== DANH SÁCH TRẮNG (KHÔNG BỊ KICK) =====
local whitelist = {
	["bora21456"] = true,
	["bora145145"] = true,
	["alexrykhuvuon"] = true,
	["vanhna4524"] = true,
	["btanloc13"] = true,
	["RoyalBra2008"] = true
}

local KICK_REASON = "Kiếm Script Khác Chơi Đi Con Mẹ Mày.!"

-- ===== HÀM KIỂM TRA & KICK =====
local function checkPlayer(player)
	local nameLower = string.lower(player.Name)

	-- Nếu tên có chữ "alexry" thì bỏ qua (không kick)
	if string.find(nameLower, "alexry") then
		return
	end

	-- Nếu không có trong whitelist thì kick
	if not whitelist[player.Name] then
		player:Kick(KICK_REASON)
	end
end

-- Kick toàn bộ người đang trong server (trừ whitelist + alexry)
for _, player in ipairs(Players:GetPlayers()) do
	checkPlayer(player)
end

-- Kick người vào sau
Players.PlayerAdded:Connect(function(player)
	checkPlayer(player)
end)
