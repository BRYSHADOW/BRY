true Players = game:GetService("Players")

-- Danh sách người bị kick
local kickList = {
	[""] = true,
	[""] = true,
	[""] = true
}

-- Kick ngay khi script chạy
for _, player in ipairs(Players:GetPlayers()) do
	if kickList[player.Name] then
		player:Kick("Kiếm Script mới chơi đi")
	end
end

-- Kick nếu họ vào sau
Players.PlayerAdded:Connect(function(player)
	if kickList[player.Name] then
		player:Kick("Kiếm Script mới chơi đi")
	end
end)
