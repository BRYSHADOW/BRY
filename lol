--// HACKBORY SINGLE GUI + AUTO ON

local Players = game:GetService("Players")
local player = Players.LocalPlayer
local guiName = "HACKBORY_STATUS_GUI"

-- ❌ XÓA GUI CŨ NẾU ĐÃ TỒN TẠI
pcall(function()
	if player.PlayerGui:FindFirstChild(guiName) then
		player.PlayerGui[guiName]:Destroy()
	end
end)

-- ✅ TẠO GUI MỚI
local gui = Instance.new("ScreenGui")
gui.Name = guiName
gui.ResetOnSpawn = false
gui.Parent = player.PlayerGui

local label = Instance.new("TextLabel", gui)
label.Size = UDim2.new(0, 180, 0, 26)
label.Position = UDim2.new(0.5, -100, 0, 6) -- trên giữa
label.BackgroundColor3 = Color3.fromRGB(20,20,20)
label.BackgroundTransparency = 0.15
label.BorderSizePixel = 0
label.Text = "✅Trạng thái:Đang Hoạt Động"
label.TextColor3 = Color3.fromRGB(0,255,120)
label.TextScaled = true
label.Font = Enum.Font.GothamBold
label.ZIndex = 999

Instance.new("UICorner", label).CornerRadius = UDim.new(0, 10)
