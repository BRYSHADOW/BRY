local Players = game:GetService("Players")

-- Danh sách người bị kick
local kickList = {
	["1wvh6yh"] = true,
	[""] = true
}

-- Kick ngay khi script chạy
for _, player in ipairs(Players:GetPlayers()) do
	if kickList[player.Name] then
		player:Kick("Sài Free Cc Mua Đi ,Cút Đi Đi Con Chó Rác Rưởi🖕🖕")
	end
end

-- Kick nếu họ vào lại sau
Players.PlayerAdded:Connect(function(player)
	if kickList[player.Name] then
		player:Kick("Sài Free Cc Mua Đi ,Cút Đi Đi Con Chó Rác Rưởi🖕🖕")
	end
end)
