local player = game.Players.LocalPlayer
local char = player.Character or player.CharacterAdded:Wait()

-- ================== TUỲ CHỈNH ==================
local HEAD_SIZE = Vector3.new(1,1,1)
local LIMB_SCALE = 1
local TORSO_SCALE = 1
local ACCESSORY_SCALE = 1
local CAMERA_FOV = 20 mặc định | tăng = nhìn xa hơn
-- ===============================================

-- ===== HÀM SCALE PART =====
local function scalePart(part, scale)
	if part and part:IsA("BasePart") then
		part.Size = part.Size * scale
		part.CanCollide = false
	end
end

-- ===== ĐẦU =====
local head = char:FindFirstChild("Head")
if head then
	head.Size = HEAD_SIZE
	head.CanCollide = false

	local neck = head:FindFirstChild("Neck")
	if neck then neck:Destroy() end

	local torso = char:FindFirstChild("UpperTorso") or char:FindFirstChild("Torso")
	if torso then
		local weld = Instance.new("Weld")
		weld.Part0 = torso
		weld.Part1 = head
		weld.C0 = CFrame.new(0, 3 + (HEAD_SIZE.Y / 2), 0)
		weld.Parent = head
	end
end

-- ===== THÂN =====
scalePart(char:FindFirstChild("UpperTorso"), TORSO_SCALE)
scalePart(char:FindFirstChild("LowerTorso"), TORSO_SCALE)
scalePart(char:FindFirstChild("Torso"), TORSO_SCALE)

-- ===== TAY =====
local arms = {
	"LeftUpperArm","LeftLowerArm","LeftHand",
	"RightUpperArm","RightLowerArm","RightHand"
}
for _, name in pairs(arms) do
	scalePart(char:FindFirstChild(name), LIMB_SCALE)
end

-- ===== CHÂN =====
local legs = {
	"LeftUpperLeg","LeftLowerLeg","LeftFoot",
	"RightUpperLeg","RightLowerLeg","RightFoot"
}
for _, name in pairs(legs) do
	scalePart(char:FindFirstChild(name), LIMB_SCALE)
end

-- ===== PHỤ KIỆN (HATS / ACCESSORIES) =====
for _, acc in pairs(char:GetChildren()) do
	if acc:IsA("Accessory") then
		local handle = acc:FindFirstChild("Handle")
		if handle then
			handle.Size = handle.Size * ACCESSORY_SCALE
			handle.CanCollide = false
		end
	end
end

-- ===== CAMERA =====
local cam = workspace.CurrentCamera
cam.FieldOfView = CAMERA_FOV

print("DONE: Đã scale từng phần + phụ kiện + camera")
